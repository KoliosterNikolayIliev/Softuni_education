function findFlavor(pies, flavor1, flavor2) {
    let start = pies.indexOf(flavor1);
    let end = pies.indexOf(flavor2) + 1;
    let sliced = pies.slice(start, end);
    return sliced;

}

findFlavor(['Pumpkin Pie',
        'Key Lime Pie',
        'Cherry Pie',
        'Lemon Meringue Pie',
        'Sugar Cream Pie'],
    'Key Lime Pie',
    'Lemon Meringue Pie'
);
findFlavor(['Apple Crisp',
        'Mississippi Mud Pie',
        'Pot Pie',
        'Steak and Cheese Pie',
        'Butter Chicken Pie',
        'Smoked Fish Pie'],
    'Pot Pie',
    'Smoked Fish Pie'
);