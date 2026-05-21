import { motion } from "framer-motion";

export default function KPI({
  title,
  value,
  color,
}) {

  return (

    <motion.div
      whileHover={{ scale: 1.03 }}
      className={`
        ${color}
        rounded-2xl
        shadow-lg
        p-5
        text-white
        min-h-[180px]
        flex
        flex-col
        justify-between
      `}
    >

      <div>

        <h3 className="
          text-sm
          sm:text-base
          font-medium
          opacity-90
        ">
          {title}
        </h3>

        <h1 className="
          mt-4
          text-2xl
          sm:text-3xl
          xl:text-4xl
          font-bold
          break-words
        ">

          {Number(value).toLocaleString()}

        </h1>

      </div>

      <div className="mt-6">

        <p className="
          text-xs
          sm:text-sm
          opacity-80
        ">
          Updated just now
        </p>

        <div className="mt-3">

          <div className="
            w-full
            bg-white/20
            rounded-full
            h-2
          ">

            <div
              className="
                bg-white
                h-2
                rounded-full
              "
              style={{ width: "75%" }}
            />

          </div>

          <p className="
            text-xs
            mt-2
            font-semibold
          ">
            Performance 75%
          </p>

        </div>

      </div>

    </motion.div>
  );
}