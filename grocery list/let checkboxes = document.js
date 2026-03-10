let checkboxes = document.querySelectorAll("input[type='checkbox']");

checkboxes.forEach(function(box){

box.addEventListener("change", function(){

let task = this.nextElementSibling;

task.classList.toggle("completed");

});

});