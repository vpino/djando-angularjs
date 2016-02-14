(function () {
  'use strict';

  /*
  
    * defino el módulo thinkster.authentication y
    * thinkster.authentication.controllers y thinkster.authentication.services
     como dependencias.
  */
  angular
    .module('thinkster.authentication', [
      'thinkster.authentication.controllers',
      'thinkster.authentication.services'
    ]);

  angular
    .module('thinkster.authentication.controllers', []);

  angular
    .module('thinkster.authentication.services', ['ngCookies']);
})();