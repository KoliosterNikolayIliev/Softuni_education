import {deleteRecord} from '../api/data.js';

export async function deletePage(context) {
    let id = context.params.id;
    const confirmed = confirm('Are you sure?');
    if (confirmed) {
        await deleteRecord(id, context);
        context.page.redirect('/allItems');
    }
}