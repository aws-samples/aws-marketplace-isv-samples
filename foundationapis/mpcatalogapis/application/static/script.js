function toggleContent(element) {
    var content = element.nextElementSibling; 
    if (content.style.display === 'none') {
        content.style.display = 'block'; 
        element.classList.remove('collapsed');
        element.classList.add('expanded');
    } else {
        content.style.display = 'none'; 
        element.classList.remove('expanded');
        element.classList.add('collapsed');
    }

}