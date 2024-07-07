{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "ef2efcaa-e3e1-4aa9-8116-f46fc40b4330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ballot ID', 'County', 'Candidate']\n",
      "Election Results\n",
      "-------------------------\n",
      "Total Votes 369711\n",
      "-------------------------\n",
      "\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "\n",
      "Diana DeGette: 73.812% (272892)\n",
      "\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "-------------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import os\n",
    "\n",
    "\n",
    "# Files to load and output\n",
    "file_to_load = os.path.join(\".\", \"Resources\", \"election_data.csv\")\n",
    "file_to_output = os.path.join(\".\", \"election_analysis.txt\")\n",
    "\n",
    "#Total Vote Counter\n",
    "total_votes = 0\n",
    "\n",
    "# Candidate Options and Vote Counters\n",
    "candidate_votes = {}\n",
    "candidate_options = []\n",
    "\n",
    "# Winning Candidate and Winning Count Tracker\n",
    "winning_candidate = \"\"\n",
    "winning_count = 0\n",
    "\n",
    "with open(file_to_load) as election_data:\n",
    "    reader = csv.reader(election_data)\n",
    "\n",
    "    # Read the header\n",
    "    header = next(reader)\n",
    "    print(header)\n",
    "\n",
    "    for row in reader:\n",
    "        # Add to the total vote count\n",
    "        total_votes = total_votes + 1\n",
    "        #print(row)\n",
    "\n",
    "        #Get the candidate name from each row\n",
    "        candidate_name = row[2]\n",
    "\n",
    "        # if candidate doesn't match any existing candidate..\n",
    "        # in a way our loop is discovering candidates as it goes\n",
    "\n",
    "        if candidate_name not in candidate_options:\n",
    "\n",
    "            # Add it the list of candidate in the running\n",
    "            candidate_options.append(candidate_name)\n",
    "\n",
    "            candidate_votes[candidate_name] = 0\n",
    "\n",
    "        candidate_votes[candidate_name] += 1\n",
    "            \n",
    " \n",
    "\n",
    "            \n",
    "\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    election_results = (\n",
    "        f\"Election Results\\n\"\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Total Votes {total_votes}\\n\"  \n",
    "        f\"-------------------------\\n\"\n",
    "    \n",
    "    )\n",
    "    print(election_results)\n",
    "\n",
    "    txt_file.write(election_results)\n",
    "\n",
    "    for candidate in candidate_votes:\n",
    "\n",
    "        votes = candidate_votes[candidate]\n",
    "        vote_percentage = float(votes) / float(total_votes) * 100\n",
    "\n",
    "        if(votes > winning_count):\n",
    "            winning_count = votes\n",
    "            winning_candidate = candidate\n",
    "\n",
    "        voter_output = f\"{candidate}: {vote_percentage:.3f}% ({votes})\\n\"\n",
    "        \n",
    "        print(voter_output)\n",
    "\n",
    "        txt_file.write(voter_output)\n",
    "\n",
    "    winning_candidate_summary = (\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Winner: {winning_candidate}\\n\"\n",
    "        f\"-------------------------\\n\"\n",
    "      \n",
    "        \n",
    "    )\n",
    "    print(winning_candidate_summary)\n",
    "\n",
    "    txt_file.write(winning_candidate_summary)\n",
    "\n",
    "# Election Results\n",
    "# -------------------------\n",
    "# Total Votes: 369711\n",
    "# -------------------------\n",
    "# Charles Casper Stockham: 23.049% (85213)\n",
    "# Diana DeGette: 73.812% (272892)\n",
    "# Raymon Anthony Doane: 3.139% (11606)\n",
    "# -------------------------\n",
    "# Winner: Diana DeGette\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "888e8ebf-4ea0-4f93-b977-f35cd343a8da",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}