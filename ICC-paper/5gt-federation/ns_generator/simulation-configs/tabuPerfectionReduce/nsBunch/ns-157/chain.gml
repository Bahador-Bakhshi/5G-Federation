graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 2
    memory 1
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 13
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
    delay 27
    bw 156
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 65
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 120
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 131
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 151
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 132
  ]
]
