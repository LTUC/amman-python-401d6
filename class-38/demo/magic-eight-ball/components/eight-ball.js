export default function EightBall(props) {
    return (

        <div className="mx-auto my-8 bg-gray-800 rounded-full w-96 h-96">
            <p className="relative flex flex-col justify-center w-56 h-56 text-xl text-center rounded-full bg-gray-50 left-16 top-16">
                {props.answeredQuestion ? props.answeredQuestion.reply : 'Waiting...'}
            </p>
        </div>
    )
}
