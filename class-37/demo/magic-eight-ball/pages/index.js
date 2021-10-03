import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

    const [question, setQuestion] = useState("Ask me anything...");
    const [reply, setReply] = useState("Thinking...")

    function questionAskedHandler(event) {
        event.preventDefault();
        const randomReply = Math.random() > .5 ? "Yes" : "No";
        setQuestion(event.target.question.value);
        setReply(randomReply)
    }
    return (
        <div>
            <Head>
                <title>Magic Eight Ball</title>
            </Head>
            <Header />
            <main className="my-4">
                <QuestionForm onSubmit={questionAskedHandler} />
                <EightBall question={question} />
                <Response reply={reply} />
            </main>
            <Footer copyright="2021" />
        </div>
    )
}

function EightBall({ question }) {
    return <div className="relative mx-auto my-8 bg-gray-900 rounded-full h-96 w-96">
        <div className="absolute flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
            <p>{question}</p>
        </div>
    </div>
}

function Header() {
    return <header className="px-8 py-6 bg-gray-500">
        <h1 className="text-4xl text-white">Magic 8 Ball</h1>
    </header>
}

function QuestionForm(props) {
    return (
        <form onSubmit={props.onSubmit} className="flex w-1/2 p-2 mx-auto bg-gray-200">
            <input name="question" className="flex-auto pl-2" />
            <button className="px-4 py-2 bg-gray-400 text-gray-50">Ask</button>
        </form>
    )
}

function Response({ reply }) {
    return <p className="text-center">{reply}</p>
}

function Footer({ copyright }) {
    return (
        <footer className="px-8 py-6 text-white bg-gray-500">
            <p>&copy;{copyright}</p>
        </footer>
    )
}

