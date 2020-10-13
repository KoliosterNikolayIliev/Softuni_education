function expandCollapse(ev) {
    let collapseContainer = this.parentElement;
    while (this) {
        if (this.className.indexOf('collapse-container')) {
            break;
        }
        collapseContainer = collapseContainer.parentElement;
    }

    if (this.parentElement.className.indexOf('collapsed') < 0) {
        this.parentElement.className += ' collapsed';
    } else {
        collapseContainer.className =
            this.parentElement.className.replace('collapsed', '');
    }
}

function initExpand() {
    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', expandCollapse);
    });
}

initExpand();
