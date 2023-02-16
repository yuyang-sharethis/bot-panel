while IFS=, read -r URL BROWSER TIME_OFFSET; do 
  echo -e "\033[0;32m= = = = = = = = = = = = ="
  echo "Sleeping, next pview in ${TIME_OFFSET}" 
  echo "seconds"
  echo "= = = = = = = = = = = = ="
  sleep $TIME_OFFSET
  echo -e "\033[0;32mCurrent url: ${URL}"
  echo -e "\033[0;32mCurrent browser: ${BROWSER}"
  robot -d ./Results -v url:$URL -v browser:$BROWSER ./Test/safari.robot;
done < ${1}
