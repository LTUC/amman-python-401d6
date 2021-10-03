import Link from 'next/link'


export default function About() {
    return (
        <div className="flex flex-col items-center justify-center h-screen gap-4 bg-gray-200">
            <h1 className="text-4xl">We're hiring!</h1>
            <Link href="/">
                <a className="bg-gray-100 px-3 py-1.5 rounded-lg">Back to Home</a>
            </Link>
        </div>
    );
}
