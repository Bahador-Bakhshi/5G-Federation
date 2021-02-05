graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 15
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 165
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 146
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 74
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 199
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 54
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 81
  ]
]
