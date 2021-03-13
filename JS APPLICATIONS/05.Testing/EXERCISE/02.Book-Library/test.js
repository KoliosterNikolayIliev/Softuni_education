const {firefox} = require('playwright');
const {assert,expect} = require('chai');
const mockData = require('./mock-data.json');


function jsonCustom(data) {
    return {
        status: 200,
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(data)
    };
}

let browser, page; // Declare reusable variables
describe('E2E tests', function () {

    this.timeout(20000);
    before(async () => {

        browser = await firefox.launch({headless: false, slowMo:1500});
    });
    after(async () => {
        await browser.close();
    });
    beforeEach(async () => {
        page = await browser.newPage();
    });
    afterEach(async () => {
        await page.close();
    });

    it('load content', async () => {
        await page.route('**/jsonstore/collections/books', (request) => request.fulfill(jsonCustom(mockData)));
        await page.goto('http://localhost:3000/');
        await page.click('text=LOAD ALL BOOKS')
        let content = await page.content()
        expect(content).to.contains('Harry Potter and the Philosopher\'s Stone')
        expect(content).to.contains('J.K.Rowling')
        expect(content).to.contains('C# Fundamentals')
        expect(content).to.contains('Svetlin Nakov')

    });

    it('adds book', async () => {
        let book = 'Testing really sucks a lot !!!'
        let author = 'Pesho Krivia'
        await page.route('**/jsonstore/collections/books', (request) => request.fulfill(jsonCustom(mockData)));
        await page.goto('http://localhost:3000/');
        await page.fill('[name="title"]', book);
        await page.fill('[name="author"]', author);
        let [request] = await Promise.all([
            page.waitForRequest(request => request.url().includes('/collections/books') && request.method() == 'POST'),
            await page.click('text=Submit')
        ]);
        assert.equal(JSON.parse(request.postData()).author,author)
        assert.equal(JSON.parse(request.postData()).title,book)
    });
    it.only('checks book validation', async () => {
        await page.route('**/jsonstore/collections/books', (request) => request.fulfill(jsonCustom(mockData)));
        await page.goto('http://localhost:3000/');
        await page.click('text=Submit');
        let otvrad;
        await page.on('dialog', async dialog => {
            otvrad = dialog.message();
            await dialog.dismiss();
            await browser.close();
        });
        page.evaluate(() => alert('1'));
        console.log(otvrad);


        // await page.on('dialog', async dialog => {
        //     console.log(dialog.message());
        //     await dialog.dismiss();
        //     await browser.close();
        // });
        // page.evaluate(() => alert('1'));


    });
    // it('post data', async () => {
    //     let name = 'Pesho';
    //     let message = 'Testing sucks!!!';
    //     await page.route('**/jsonstore/messenger', (request) => request.fulfill(jsonCustom(mockData)));
    //     await page.goto('http://localhost:3000/');
    //     await page.fill('[id="author"]', name);
    //     await page.fill('[id="content"]', message);
    //     let [request] = await Promise.all([
    //         page.waitForRequest(request => request.url().includes('/jsonstore/messenger') && request.method() == 'POST'),
    //         page.click('text=Send')
    //     ]);
    //     assert.equal(JSON.parse(request.postData()).author,name)
    //     assert.equal(JSON.parse(request.postData()).content,message)
    //
    //
    //
    // });
});

