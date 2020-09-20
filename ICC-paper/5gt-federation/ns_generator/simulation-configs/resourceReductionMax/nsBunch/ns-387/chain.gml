graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 16
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 7
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 5
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 149
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 175
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 67
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 193
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 59
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 101
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 195
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 83
  ]
]
