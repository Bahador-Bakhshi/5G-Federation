graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 7
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 15
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 67
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 65
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 102
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 151
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 110
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 86
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 168
  ]
]
