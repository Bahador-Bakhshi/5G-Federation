graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 9
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 7
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 140
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 81
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 74
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 196
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 97
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 179
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 99
  ]
]
