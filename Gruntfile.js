module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    shell: {
        pelican: {
            command: 'pelican'
        },
        server: {
          command: 'python -m SimpleHTTPServer 8888',
          options: {
            async: true
          }
        }
    },

    watch: {
      files: ['content/**/*.md','themes/**/*.*'],
      tasks: ['shell:pelican'],
      options: {
        // Start a live reload server on the default port 35729
        livereload: true,
      }
    }
  });

  grunt.loadNpmTasks('grunt-shell-spawn');
  grunt.loadNpmTasks('grunt-contrib-watch');


  grunt.registerTask('default', ['shell:server','watch']);

};