import Link from 'next/link'

export default function Footer(props) {
    return (
        <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
            <nav>
                <Link href="/careers">
                    <a className="px-3 py-1.5 bg-gray-700 rounded-lg">Careers</a>
                </Link>
            </nav>
        </footer>
    )
}
