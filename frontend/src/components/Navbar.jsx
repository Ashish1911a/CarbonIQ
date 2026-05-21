import { FaLeaf } from "react-icons/fa";
import { FiBell } from "react-icons/fi";

export default function Navbar() {

  return (

    <nav className="bg-white shadow-md px-8 py-5 flex items-center justify-between">

      <div>

        <h1 className="text-3xl font-bold text-green-700">
          CarbonIQ
        </h1>

        <p className="text-gray-500 text-sm">
          ESG Analytics Platform
        </p>

      </div>

      <div className="text-right">

        <p className="text-gray-500 text-sm">
          Reporting Year
        </p>

        <p className="text-xl font-bold text-gray-800">
          2026
        </p>

      </div>

    </nav>
  );
}