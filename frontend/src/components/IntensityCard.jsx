import { motion } from "framer-motion";

export default function IntensityCard({ value }) {

  return (

    <motion.div
      whileHover={{ scale: 1.03 }}
      className="
        bg-gradient-to-br
        from-green-600
        to-emerald-500
        rounded-2xl
        shadow-lg
        p-5
        text-white
        min-h-[180px]
        flex
        flex-col
        justify-between
      "
    >

      <div>

        <h3 className="
          text-sm
          sm:text-base
          font-medium
          opacity-90
        ">
          Emission Intensity
        </h3>

        <div className="mt-4">

          <h1 className="
            text-3xl
            sm:text-4xl
            font-bold
          ">

            {value}

          </h1>

          <p className="
            mt-1
            text-sm
            opacity-90
          ">
            kgCO₂e / ton
          </p>

        </div>

      </div>

      <div className="mt-6">

        <p className="
          text-sm
          font-medium
        ">
          12% better than last year
        </p>

        <div className="
          mt-3
          bg-white/10
          rounded-xl
          p-3
        ">

          <p className="text-xs opacity-80">
            Formula
          </p>

          <p className="
            text-sm
            font-semibold
            mt-1
          ">
            Total Emissions ÷ Production Metric
          </p>

        </div>

      </div>

    </motion.div>
  );
}