graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 16
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 95
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 89
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 137
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 189
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 167
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 113
  ]
]
