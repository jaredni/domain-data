'use client';
import React, {useState} from "react";
import Results from "./components/results/Results";

import {fetchDomainData} from "@/app/api/DomainInformation";

export default function Home() {
  const [results, setResults] = useState(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const searchValue = (document.getElementById('search') as HTMLInputElement)?.value;
    const informationTypeValue = (document.querySelector('input[name="informationType"]:checked') as HTMLInputElement)?.value;
    if (!searchValue) {
      alert('Please enter a domain.');
      return;
    }

    const data = await fetchDomainData(searchValue, informationTypeValue);
    setResults(data.data);
  };

  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <main className="flex flex-col row-start-2 items-center sm:items-start">
        <div className="flex flex-col items-center w-full">
          <input
            type="text"
            placeholder="Search..."
            id="search"
            className="rounded-full border border-gray-300 px-8 py-4 w-140 text-lg focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
            style={{ margin: "0 auto", display: "block" }}
          />
        </div>
        <div className="flex flex-row items-center w-full gap-4 justify-center pt-1 text-gray-500">
          <label className="flex items-center gap-2">
            <input name="informationType" type="radio" className="form-radio" value="domain_information" defaultChecked={true}/>
            Domain Information
          </label>
          <label className="flex items-center gap-2">
            <input name="informationType" type="radio" className="form-radio" value="contact_information" />
            Contact Information
          </label>
        </div>
        <div className="flex flex-col items-center w-full pt-2">
          <button
            type="submit"
            className="mt-2 pt-2 rounded-full bg-blue-500 text-white px-6 py-2 text-base font-medium hover:bg-blue-600 transition-colors"
            style={{ margin: "0 auto", display: "block" }}
            onClick={handleSubmit}
          >
            Submit
          </button>
        </div>
        {results && (
            <div className="flex flex-col items-center w-full pt-2">
              <Results result={results} />
            </div>
        )}
      </main>
    </div>
  );
}
