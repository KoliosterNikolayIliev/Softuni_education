const {firefox} = require('playwright');
const {assert} = require('chai');
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

    this.timeout(6000);
    before(async () => {

        browser = await firefox.launch({headless: false, slowMo: 1});
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
        await page.route('**/jsonstore/messenger', (request) => request.fulfill(jsonCustom(mockData)));
        await page.goto('http://localhost:3000/');
        await page.click('text=LOAD ALL BOOKS');
        const firstBook = page.waitFor('text=Harry Potter and the Philosopher\'s Stone')
        assert.equal(firstBook, true);


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

