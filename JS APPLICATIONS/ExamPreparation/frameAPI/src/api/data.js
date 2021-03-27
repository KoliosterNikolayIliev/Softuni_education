import * as api from './api.js';

import {host} from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

async function getItems() {
    return await api.get(host+'/data/catalog');
}

async function getItemId(id) {
    return await api.get(host+'/data/catalog/' + id);
}

async function getUserItems() {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host+`/data/catalog?where=_ownerId%3D%22${userId}%22`);
}

async function createRecord(data) {
    return await api.post(host+'/data/catalog', data);
}

async function editRecord(id, data) {
    return await api.put(host+'/data/catalog/' + id, data);
}

async function deleteRecord(id) {
    // TODO Check if id exists!!!
    return await api.del(host+'/data/catalog/' + id);
}

export {
    getItems,
    getItemId,
    getUserItems,
    createRecord,
    editRecord,
    deleteRecord,
}

// //for testing purposes
// window.login=login
// window.register=register
// window.logout=logout
// window.getItems=getItems
// window.getItemId=getItemId
// window.getUserItems=getUserItems
// window.createRecord=createRecord
// window.editRecord=editRecord
// window.deleteRecord=deleteRecord

