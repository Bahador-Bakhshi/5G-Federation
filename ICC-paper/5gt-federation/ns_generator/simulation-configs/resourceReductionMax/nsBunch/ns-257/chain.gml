graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 7
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 103
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 200
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 150
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 134
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 78
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 189
  ]
]
