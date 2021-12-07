import {useSelector, useDispatch} from 'react-redux';


import {increase, reset} from '../store/votes'

const Voting = () => {
    const state = useSelector(state => {
        return {
            candidates : state.voteReducer.candidates,
        }
    });

    const dispatch = useDispatch();


    return (
        <>
        <ul>
            {
                state.candidates.map( candidate =>{
                    return(

                        <>
                        <li onClick={()=> dispatch(increase(candidate.name))}>  {candidate.name} : {candidate.votes}</li>
                        </>
                    )
                })
            }
         </ul>
         <button onClick={()=>{dispatch(reset())}}>Reset </button>
        </>
    )
}

export default Voting;