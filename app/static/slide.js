const slides = document.querySelector('.slides');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');
let currentIndex = 0;

function showSlide(index) {
  slides.style.transform = `translateX(-${index * 100}%)`;
}

prevButton.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + 3) % 3;
  showSlide(currentIndex);
});

nextButton.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % 3;
  showSlide(currentIndex);
});

showSlide(currentIndex);
