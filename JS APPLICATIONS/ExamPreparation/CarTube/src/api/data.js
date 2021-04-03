import * as api from './api.js';

import {host} from './api.js';


async function login(username, password) {
    return await api.apiLogin(host + '/users/login',username,password);
}

async function register(username, password) {
    return await api.apiRegister(host + '/users/register',username,password);
}

function logout() {
    return api.apiLogout(host + '/users/logout');
}

async function getItems() {
    return await api.get(host + '/data/cars?sortBy=_createdOn%20desc');
}

async function getItemId(id) {
    return await api.get(host + '/data/cars/' + id);
}

async function getUserItems() {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host + `/data/cars?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}

async function createRecord(data) {
    return await api.post(host + '/data/cars', data);
}

async function editRecord(id, data) {
    return await api.put(host + '/data/cars/' + id, data);
}

async function deleteRecord(id) {
    // TODO Check if id exists!!!
    return await api.del(host + '/data/cars/' + id);
}

async function getsearchItems(query) {
    return await api.get(host + `/data/cars?where=year%3D${query}`);
}

export {
    getItems,
    getItemId,
    getUserItems,
    createRecord,
    editRecord,
    deleteRecord,
    login,
    register,
    logout,
    getsearchItems
};

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
window.getsearchItems=getsearchItems

