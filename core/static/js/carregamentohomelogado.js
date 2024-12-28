
function redirecionarApos3Segundos(url) {
    setTimeout(() => {
        window.location.href = url;  
    }, 1500); 
}

document.addEventListener('DOMContentLoaded', () => {
    redirecionarApos3Segundos('/home_logado/');  
});
