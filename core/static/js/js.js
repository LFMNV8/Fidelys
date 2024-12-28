document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector('.header');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const threshold = 50; 

 
    window.addEventListener('scroll', function () {
        if (window.scrollY > threshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    
    navbarToggler.addEventListener('click', function () {
        const isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
        if (isExpanded) {
            header.classList.remove('menu-open');
        } else {
            header.classList.add('menu-open');
        }
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add("show");
        }, index * 300); 
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const fadeIns = document.querySelectorAll('.fade-in');

    function handleScroll() {
        fadeIns.forEach(element => {
            const rect = element.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight - 50 && rect.bottom > 0;

            if (isVisible) {
                element.classList.add('appear');
            } else {
                element.classList.remove('appear'); 
            }
        });
    }

    
    window.addEventListener('scroll', handleScroll);

    
    handleScroll();
});




