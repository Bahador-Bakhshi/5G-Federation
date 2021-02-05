graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 15
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 12
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 9
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 131
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 200
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 60
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 74
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 176
  ]
]
