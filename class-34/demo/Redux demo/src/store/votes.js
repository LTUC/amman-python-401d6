// 1. create init state
 
const initState = {
    candidates : [
        {name: 'Bashar', votes: 0 },
        {name: 'Ehab', votes: 0},
        {name: 'Jehad', votes: 0}
 
    ],
    totalVotes: 0
}

// 2. create actions
        
 
  // action is function that return an object {type, payload}
  // increase, reset
export const increase = (name)   =>{
    return {
        type: 'INCREASE',
        payload: name
    }
}

export const reset = () =>{
    return {
        type: 'RESET',
        payload: null
        }

}


// 3. create reducer

const voteReducer = (state= initState, action) =>{
    const {type, payload} = action;

    switch(type){
       case 'INCREASE':
           const totalVotes = state.totalVotes +1;

           const candidates = state.candidates.map( candidate =>{
               if(candidate.name == payload) return {name: candidate.name , votes: candidate.votes +1}
               else return candidate;
           })

           return {totalVotes, candidates}


       case 'RESET':
              return initState;

       default:
           return state; 
    }

}

export default voteReducer;