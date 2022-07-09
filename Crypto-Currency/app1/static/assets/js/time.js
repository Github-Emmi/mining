(function(){
    'use strict';

    var monthName = new Array('January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');
    var hourap = new Array(12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11);

    const dateObj = new Date();
    var day = dateObj.getDate(), 
        month = dateObj.getMonth(), 
        year = dateObj.getFullYear(), 
        hour = dateObj.getHours(), 
        minutes = dateObj.getMinutes(),
        secundes = dateObj.getSeconds();
        

document.addEventListener('DOMContentLoaded', function(){
    var c = document.getElementById('clock');
    c.innerHTML = dateObj;
});
})();