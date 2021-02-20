document.body.innerHTML = `
<main>
    <div class="wrapper">
        <section>
            <div>
                <h1 class="gray">Add Task</h1>
            </div>
            <div>
                <form action="">
                    <label for="task">Task</label><br>
                    <input type="text" id="task" name="task" placeholder="JS Advanced Exam"><br>
                    <label for="description">Description</label><br>
                    <textarea id="description" placeholder="Lern DOM, Unit Testing and Classes"></textarea>
                    <label for="date">Due Date</label><br>
                    <input type="text" id="date" name="date" placeholder="2020.04.08"><br>
                    <button id="add">Add</button>
                </form>
            </div>
        </section>

        <section>
            <div>
                <h1 class="orange">Open</h1>
            </div>
            <div>
                
            </div>
        </section>
        <section>
            <div>
                <h1 class="yellow">In Progress</h1>
            </div>
            <div id="in-progress">
                
            </div>
        </section>
        <section>
            <div>
                <h1 class="green">Complete</h1>
            </div>
            <div>
                
            </div>
        </section>
    </div>
</main>
`;

result();

let elements = {
    task: document.getElementById("task"),
    description: document.getElementById("description"),
    date: document.getElementById("date"),
}
elements["addButton"] = document.getElementById("add");

elements.task.value = "JS Advanced FinalExam";
elements.description.value = "Lern DOM, Unit Testing and Classes";
elements.date.value = "2020.04.08";

let sections = document.getElementsByTagName("section");
let open = sections[1];
let inProgress = sections[2];
let complete = sections[3];

elements.addButton.click();

assert.equal(open.children.length, 2, "Incorrect count of added tasks in 'Open' section");
assert.equal(open.children[1].children[0].tagName, "ARTICLE", "Incorrect tagname");
assert.equal(open.children[1].children[0].children.length, 4, "Incorrect count of added HTML Elements in the article tag");
assert.equal(open.children[1].children[0].children[0].textContent, "JS Advanced FinalExam", "Incorrect Task name");
assert.equal(open.children[1].children[0].children[1].textContent, "Description: Lern DOM, Unit Testing and Classes", "Incorrect description");
assert.equal(open.children[1].children[0].children[2].textContent, "Due Date: 2020.04.08", "Incorrect date");
assert.equal(open.children[1].children[0].children[3].children.length, 2, "Incorrect count of buttons");

let delBtn = open.children[1].children[0].children[3].children[1];
delBtn.click();

//testing if task is deleted
assert.equal(open.children[1].children.length, 0, "Incorrect count of children elements in 'Open' section");