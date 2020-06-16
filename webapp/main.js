console.log('Hello world');

const form = document.getElementById('user-form');
console.log(form);

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const username = formData.get('username');
  console.log(username);
});
