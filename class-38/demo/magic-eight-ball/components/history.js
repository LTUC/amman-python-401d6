export default function History({ answeredQuestions }) {
    return (
        <table className="w-1/2 mx-auto border-4 border-collapse border-gray-500">
            <thead>
                <tr>
                    <th className="border border-black">No.</th>
                    <th className="border border-black">Question</th>
                    <th className="border border-black">Response</th>
                </tr>
            </thead>
            <tbody>


                {answeredQuestions.map(item => (
                    <tr key={item.id} className="odd:bg-gray-300">
                        <td className="pl-2 border border-black">{item.id}</td>
                        <td className="pl-2 border border-black">{item.question}</td>
                        <td className="pl-2 border border-black">{item.reply}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}
