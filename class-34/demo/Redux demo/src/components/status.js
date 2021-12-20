import {useSelector} from 'react-redux';


const Status = () =>{
    const state = useSelector((state) =>{
        console.log(state)
        return {
            votes: state.voteReducer.totalVotes,
        }

    })


    return <p>Total of Votes: {state.votes} </p>
}

export default Status;