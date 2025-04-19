// Количество строк и столбцов
const rows = 5;
const cols = 8;

// Цикл для формирования прямоугольника
for (let i = 0; i < rows; i++) {
  let row = '';
  for (let j = 0; j < cols; j++) {
    row += 'A';
  }
  console.log(row); // Вывод строки в консоль
}


// Получение элемента body
const body = document.body;

// Цикл для формирования прямоугольника
for (let i = 0; i < rows; i++) {
  let row = '';
  for (let j = 0; j < cols; j++) {
    row += 'A';
  }
  
  // Создаем элемент <div> для строки и добавляем на страницу
  const div = document.createElement('div');
  div.textContent = row;
  body.appendChild(div);
}
