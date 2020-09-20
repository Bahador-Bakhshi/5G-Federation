graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 2
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 13
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 56
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 134
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 50
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 98
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 83
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 87
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 96
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 179
  ]
]
