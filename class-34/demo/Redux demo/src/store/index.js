// 4. building our store

import {createStore, combineReducers} from 'redux';
import voteReducer from './votes'


const reducers = combineReducers({voteReducer});

const store = () => {
    return createStore(reducers);
}

export default store();