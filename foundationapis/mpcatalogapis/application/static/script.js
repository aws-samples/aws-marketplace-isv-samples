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

function openTab(event, tabName) {
    var i, tabContent, tabLinks;

    tabContent = document.getElementsByClassName('tab-content');
    for(i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }

    tabLinks = document.getElementsByClassName('tab-link');
    for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className.replace("active", "");
    }

    document.getElementById(tabName).style.display = "block"; 
    event.currentTarget.className = "active"

}

function goback() {
    window.history.back()
}

var selectElement = document.getElementById("categories");
Array.from(selectElement.options).forEach(function(option) {
    option.addEventListener('mousedown', function(event) {
        event.preventDefault();
        this.selected = !this.selected; 
    });
});
