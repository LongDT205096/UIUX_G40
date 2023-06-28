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