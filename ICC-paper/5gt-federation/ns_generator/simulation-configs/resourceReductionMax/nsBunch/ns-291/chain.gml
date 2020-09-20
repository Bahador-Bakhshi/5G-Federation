graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 55
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 177
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 54
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 190
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 196
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 103
  ]
]
