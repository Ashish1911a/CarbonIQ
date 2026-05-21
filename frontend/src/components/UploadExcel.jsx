import { useState } from "react";
import api from "../api";

export default function UploadExcel() {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [message, setMessage] = useState("");

  const handleUpload = async () => {

  if (!file) {
    setMessage("Please select an Excel file");
    return;
  }

  try {

    setLoading(true);

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/upload-excel",
      formData
    );

    console.log(response.data);

    setMessage(
      `Upload successful! ${response.data.records_inserted} records inserted`
    );

    setTimeout(() => {
      window.location.reload();
    }, 1500);

  } catch (error) {

    console.error(error);

    if (error.response) {
      console.log(error.response.data);
    }

    setMessage("Upload failed");

  } finally {

    setLoading(false);

  }
};

  return (

    <div className="bg-white p-6 rounded-2xl shadow-lg">

      <h2 className="text-2xl font-bold text-gray-800 mb-4">
        Upload Excel Data
      </h2>

      <input
        type="file"
        accept=".xlsx,.xls"
        onChange={(e) => setFile(e.target.files[0])}
        className="
          w-full
          bg-gray-100
          p-3
          rounded-xl
          border
          border-gray-300
          mb-4
        "
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="
          w-full
          bg-green-600
          hover:bg-green-700
          transition-all
          duration-300
          text-white
          font-semibold
          py-3
          rounded-xl
        "
      >

        {loading ? "Uploading..." : "Upload Excel"}

      </button>

      {message && (
        <div className="mt-4 text-center text-green-700 font-semibold">
          {message}
        </div>
      )}

    </div>
  );
}