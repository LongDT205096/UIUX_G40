const select = document.getElementById('Task_haha');
const element = document.getElementById('my-element');

select.addEventListener('change', function() {
  const selectedValue = select.value;
  if (selectedValue === "ProjectTask") {
    element.style.display = 'block';
  } else {
    element.style.display = 'none';
  }
});

const select_1 = document.getElementById('type');
const element_1 = document.getElementById('project-add');

select_1.addEventListener('change', function() {
  const selectedValue = select_1.value;
  if (selectedValue === "pjtask") {
    element_1.style.display = 'block';
  } else {
    element_1.style.display = 'none';
  }
});
