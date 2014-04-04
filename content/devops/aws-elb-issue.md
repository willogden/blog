Title: AWS Elastic Load Balancer connections dropped issue
Date: 2014-02-23 14:05
Category: DevOps
Tags: devops
Slug: aws-elb-issue
Author: Will Ogden
Summary: AWS Elastic Load Balancer rudely drops connections on instance removal...

Over at TrustedHousesitters.com we use Fabric to deploy changes to our AWS infrastructure. The configuration was nice and simple and it worked fine - however it had been setup to deploy to all the production servers in parallel, which effectively brought the site down (even if it did just show a friendly 503 page). As we use an ELB, the simple solution appeared to just be a rolling update; popping the instance out of the ELB, updating the code, then re-adding e.g.

    @fab.task
    @fab.serial
    def rolling_deploy():
        remove_from_load_balancer(False)
        install_code()
        run_app()
        add_to_load_balancer(False)

    @fab.task
    def add_to_load_balancer(ask_confirm=True):
        """Add selected instances to the ELB"""
        instance = get_instance_by_dns_name(fab.env.host_string)
        print green("Found instance ID {instance_id}".format(instance_id=instance.id))

        if ask_confirm:
            if not confirm(red("Are you sure you wish to add this instance to the load balancer \"{load_balancer_name}\"?".format(load_balancer_name=LOAD_BALANCER_NAMES[fab.env.deployment_type])), default=False):
            fab.abort(red("Aborting at user request"))

        balancer = elb_conn.get_all_load_balancers(load_balancer_names=[LOAD_BALANCER_NAMES[fab.env.deployment_type]])[0]
        balancer.register_instances([instance.id])

        print green("Instance ID {instance_id} added to \"{load_balancer_name}\" load balancer OK".format(instance_id=instance.id,load_balancer_name=LOAD_BALANCER_NAMES[fab.env.deployment_type]))

    @fab.task
    def remove_from_load_balancer(ask_confirm=True):
        """Remove selected instances to the ELB"""
        instance = get_instance_by_dns_name(fab.env.host_string)
        print green("Found instance ID {instance_id}".format(instance_id=instance.id))

        if ask_confirm:
            if not confirm(red("Are you sure you wish to remove this instance from the load balancer \"{load_balancer_name}\"?".format(load_balancer_name=LOAD_BALANCER_NAMES[fab.env.deployment_type])), default=False):
                fab.abort(red("Aborting at user request"))

        balancer = elb_conn.get_all_load_balancers(load_balancer_names=[LOAD_BALANCER_NAMES[fab.env.deployment_type]])[0]
        balancer.deregister_instances([instance.id])

        print green("Instance ID {instance_id} removed from \"{load_balancer_name}\" load balancer OK".format(instance_id=instance.id,load_balancer_name=LOAD_BALANCER_NAMES[fab.env.deployment_type]))

After setting up a very simple load test using [Gatling](http://gatling-tool.org/) (which is awesome by the way - no more JMeter, just simple Scala code), we noticed that when an instance was removed from the ELB any active connections were just dropping. After digging around this appears to be a known issue that's been around for 3 years! [https://forums.aws.amazon.com/thread.jspa?threadID=61278&tstart=0](https://forums.aws.amazon.com/thread.jspa?threadID=61278&tstart=0). There doesn't seem to be any work arounds short of having another ELB setup and flip flopping DNS, so we're stuck with it for now. Possibly the only solution is to move to HAProxy/Hipache or similar; the downside being the ELB is more competitively priced.
