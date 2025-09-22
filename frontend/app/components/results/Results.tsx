import React from "react";

interface Result {
    information_type: string;
    domain_name?: string;
    registrar_name?: string;
    created_date?: string;
    expires_date?: string;
    estimated_domain_age?: number;
    host_names?: string;
    contact_email?: string;
    registrant_name?: string;
    technical_contact_name?: string;
}

interface ResultsProps {
    domainName: string;
    result: Result;
}

const Results = ({domainName, result}: ResultsProps) => {
    const formatKey = (key: string): string => {
        return key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    }

    return (
        <div className="results">
            <p className="text-4xl">{formatKey(result.information_type)} for <span className="font-bold">{domainName}</span></p>
            <div className="bg-gray-100 rounded-lg shadow p-6 mt-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {Object.entries(result)
                        .filter(([key]) => key !== "information_type")
                        .map(([key, value]) => (
                            <div key={key} className="flex flex-col mb-2">
                                <span className="font-semibold">{formatKey(key)}</span>
                                <span className="text-gray-700">{value as string}</span>
                            </div>
                        ))}
                </div>
            </div>
        </div>
    );
}

export default Results;
