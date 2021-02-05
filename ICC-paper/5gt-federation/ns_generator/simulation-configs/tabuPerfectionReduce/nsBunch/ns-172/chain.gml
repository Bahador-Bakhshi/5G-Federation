graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 13
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 7
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 190
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 81
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 118
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 98
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 146
  ]
  edge [
    source 2
    target 5
    delay 35
    bw 84
  ]
]
