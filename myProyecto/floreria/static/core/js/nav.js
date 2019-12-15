const navSlide=()=>{
    const telefono=document.querySelector('.telefono');
    const nav=document.querySelector('.link');

    telefono.addEventListener('click',()=>{
        nav.classList.toggle('nav-active');

    });
}

navSlide();