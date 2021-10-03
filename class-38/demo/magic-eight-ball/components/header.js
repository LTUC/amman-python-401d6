export default function Header({ answerCount }) {
    return (
        <header className="flex items-center justify-between w-full px-8 py-4 text-center text-gray-100 bg-gray-500">
            <h1 className="text-4xl ">Magic 8 Ball</h1>
            <h2>{answerCount} questions answered</h2>
        </header>
    )
}
