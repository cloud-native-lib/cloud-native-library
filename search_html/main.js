var books = [{"titre": "titre1"}, {"titre": "titre2"}, {"titre": "titre3"}];
var titles = []
for (var book = 0; book < books.length; book++){
    titles.push(books[book]['titre'])
};

// const selectElement = document.querySelector('.ice-cream');

// selectElement.addEventListener('change', (event) => {
//   const result = document.querySelector('.result');
//   result.textContent = `You like ${event.target.value}`;
// });


// console.log(titles)