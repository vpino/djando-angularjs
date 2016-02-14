(function () {
  'use strict';

  angular
    .module('thinkster.routes')
    .config(config);

  //Dependencia un metodo de angular para poder enrutar
  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  * .otherwise: Esto retorna a una ruta en caso de error
    * en este ejemplo retorna a / raiz
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/register.html'
    }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/login.html'
    }).otherwise('/');
  }



  
})();
